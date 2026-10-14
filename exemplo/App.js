import { Alert, Platform, ScrollView, Text, View } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { SafeAreaProvider, SafeAreaView } from 'react-native-safe-area-context';
import CartaoEvento from './components/CartaoEvento';
import styles from './styles';

const evento = {
  nome: 'Encontro de Tecnologia',
  data: '21 de outubro de 2026, às 19h',
  local: 'Auditório do campus',
  descricao: 'Uma conversa sobre aplicativos, criatividade e soluções para o dia a dia.',
  imagem: require('./assets/evento.png'),
};

export default function App() {
  function mostrarInteresse() {
    const mensagem = `Você demonstrou interesse em ${evento.nome}. Esta é uma simulação: nenhuma inscrição foi enviada.`;
    if (Platform.OS === 'web') {
      globalThis.alert(mensagem);
      return;
    }
    Alert.alert('Interesse demonstrado', mensagem, [{ text: 'Entendi' }]);
  }

  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.safe}>
        <StatusBar style="dark" />
        <ScrollView contentContainerStyle={styles.pagina}>
          <View style={styles.conteudo}>
            <Text style={styles.etiqueta}>EVENTOS DO CAMPUS</Text>
            <Text style={styles.titulo}>Vamos aprender juntos?</Text>
            <Text style={styles.introducao}>Conheça o encontro e toque no botão para experimentar a interação.</Text>
            <CartaoEvento evento={evento} onInteresse={mostrarInteresse} />
            <Text style={styles.rodape}>Atividade prática 2 • Professor Edilberto Firmino</Text>
            <Text style={styles.aviso}>Evento fictício para fins didáticos.</Text>
          </View>
        </ScrollView>
      </SafeAreaView>
    </SafeAreaProvider>
  );
}
