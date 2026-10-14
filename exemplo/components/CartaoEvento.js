import { Image, Pressable, Text, View } from 'react-native';
import styles from '../styles';

export default function CartaoEvento({ evento, onInteresse }) {
  return (
    <View style={styles.cartao}>
      <Image
        source={evento.imagem}
        style={styles.imagem}
        resizeMode="cover"
        accessibilityLabel="Ilustração de um encontro de tecnologia"
      />
      <View style={styles.detalhes}>
        <Text style={styles.categoria}>OFICINA • TECNOLOGIA</Text>
        <Text style={styles.nome}>{evento.nome}</Text>
        <Text style={styles.informacao}>Data: {evento.data}</Text>
        <Text style={styles.informacao}>Local: {evento.local}</Text>
        <Text style={styles.descricao}>{evento.descricao}</Text>
        <Pressable
          onPress={onInteresse}
          accessibilityRole="button"
          accessibilityLabel={`Demonstrar interesse em ${evento.nome}`}
          style={({ pressed }) => [styles.botao, pressed && styles.botaoPressionado]}
        >
          <Text style={styles.textoBotao}>Tenho interesse</Text>
        </Pressable>
      </View>
    </View>
  );
}
