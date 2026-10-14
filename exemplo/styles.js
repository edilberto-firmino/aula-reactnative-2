import { StyleSheet } from 'react-native';

export default StyleSheet.create({
  safe: { flex: 1, backgroundColor: '#eff6ff' },
  pagina: { padding: 24, flexGrow: 1 },
  conteudo: { width: '100%', maxWidth: 680, alignSelf: 'center' },
  etiqueta: { color: '#1d4ed8', fontSize: 12, fontWeight: '700', marginBottom: 12 },
  titulo: { fontSize: 30, fontWeight: '700', color: '#122542', marginBottom: 12 },
  introducao: { fontSize: 16, lineHeight: 24, color: '#475569', marginBottom: 24 },
  cartao: { backgroundColor: '#fff', borderRadius: 18, overflow: 'hidden', borderWidth: 1, borderColor: '#dbe4ef' },
  imagem: { width: '100%', aspectRatio: 2 },
  detalhes: { padding: 20, gap: 12 },
  categoria: { fontSize: 12, color: '#1d4ed8', fontWeight: '700' },
  nome: { fontSize: 24, fontWeight: '700', color: '#122542' },
  informacao: { fontSize: 16, lineHeight: 24, color: '#334155' },
  descricao: { fontSize: 16, lineHeight: 24, color: '#475569' },
  botao: { backgroundColor: '#1d4ed8', borderRadius: 10, minHeight: 48, padding: 14, alignItems: 'center', justifyContent: 'center', marginTop: 4 },
  botaoPressionado: { opacity: 0.7 },
  textoBotao: { color: '#fff', fontSize: 16, fontWeight: '700', textAlign: 'center' },
  rodape: { fontSize: 14, lineHeight: 22, color: '#475569', textAlign: 'center', marginTop: 24 },
  aviso: { fontSize: 12, color: '#475569', textAlign: 'center', marginTop: 8 },
});
