"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ImportKeyMaterial``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.import_as2805_key_cryptogram
    import capo_payment_cryptography.types.import_diffie_hellman_tr31_key_block
    import capo_payment_cryptography.types.import_key_cryptogram
    import capo_payment_cryptography.types.import_tr31_key_block
    import capo_payment_cryptography.types.import_tr34_key_block
    import capo_payment_cryptography.types.root_certificate_public_key
    import capo_payment_cryptography.types.trusted_certificate_public_key


class _ImportKeyMaterial_RootCertificatePublicKey(TypedDict, closed=True):
    RootCertificatePublicKey: "capo_payment_cryptography.types.root_certificate_public_key.RootCertificatePublicKey"


class _ImportKeyMaterial_TrustedCertificatePublicKey(TypedDict, closed=True):
    TrustedCertificatePublicKey: "capo_payment_cryptography.types.trusted_certificate_public_key.TrustedCertificatePublicKey"


class _ImportKeyMaterial_Tr31KeyBlock(TypedDict, closed=True):
    Tr31KeyBlock: (
        "capo_payment_cryptography.types.import_tr31_key_block.ImportTr31KeyBlock"
    )


class _ImportKeyMaterial_Tr34KeyBlock(TypedDict, closed=True):
    Tr34KeyBlock: (
        "capo_payment_cryptography.types.import_tr34_key_block.ImportTr34KeyBlock"
    )


class _ImportKeyMaterial_KeyCryptogram(TypedDict, closed=True):
    KeyCryptogram: (
        "capo_payment_cryptography.types.import_key_cryptogram.ImportKeyCryptogram"
    )


class _ImportKeyMaterial_DiffieHellmanTr31KeyBlock(TypedDict, closed=True):
    DiffieHellmanTr31KeyBlock: "capo_payment_cryptography.types.import_diffie_hellman_tr31_key_block.ImportDiffieHellmanTr31KeyBlock"


class _ImportKeyMaterial_As2805KeyCryptogram(TypedDict, closed=True):
    As2805KeyCryptogram: "capo_payment_cryptography.types.import_as2805_key_cryptogram.ImportAs2805KeyCryptogram"


ImportKeyMaterial: TypeAlias = (
    _ImportKeyMaterial_RootCertificatePublicKey
    | _ImportKeyMaterial_TrustedCertificatePublicKey
    | _ImportKeyMaterial_Tr31KeyBlock
    | _ImportKeyMaterial_Tr34KeyBlock
    | _ImportKeyMaterial_KeyCryptogram
    | _ImportKeyMaterial_DiffieHellmanTr31KeyBlock
    | _ImportKeyMaterial_As2805KeyCryptogram
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportKeyMaterial) -> dict:
    if "RootCertificatePublicKey" in value:
        import capo_payment_cryptography.types.root_certificate_public_key

        return {
            "RootCertificatePublicKey": capo_payment_cryptography.types.root_certificate_public_key.serialize_aws_json_1_0(
                value["RootCertificatePublicKey"]
            )
        }
    elif "TrustedCertificatePublicKey" in value:
        import capo_payment_cryptography.types.trusted_certificate_public_key

        return {
            "TrustedCertificatePublicKey": capo_payment_cryptography.types.trusted_certificate_public_key.serialize_aws_json_1_0(
                value["TrustedCertificatePublicKey"]
            )
        }
    elif "Tr31KeyBlock" in value:
        import capo_payment_cryptography.types.import_tr31_key_block

        return {
            "Tr31KeyBlock": capo_payment_cryptography.types.import_tr31_key_block.serialize_aws_json_1_0(
                value["Tr31KeyBlock"]
            )
        }
    elif "Tr34KeyBlock" in value:
        import capo_payment_cryptography.types.import_tr34_key_block

        return {
            "Tr34KeyBlock": capo_payment_cryptography.types.import_tr34_key_block.serialize_aws_json_1_0(
                value["Tr34KeyBlock"]
            )
        }
    elif "KeyCryptogram" in value:
        import capo_payment_cryptography.types.import_key_cryptogram

        return {
            "KeyCryptogram": capo_payment_cryptography.types.import_key_cryptogram.serialize_aws_json_1_0(
                value["KeyCryptogram"]
            )
        }
    elif "DiffieHellmanTr31KeyBlock" in value:
        import capo_payment_cryptography.types.import_diffie_hellman_tr31_key_block

        return {
            "DiffieHellmanTr31KeyBlock": capo_payment_cryptography.types.import_diffie_hellman_tr31_key_block.serialize_aws_json_1_0(
                value["DiffieHellmanTr31KeyBlock"]
            )
        }
    elif "As2805KeyCryptogram" in value:
        import capo_payment_cryptography.types.import_as2805_key_cryptogram

        return {
            "As2805KeyCryptogram": capo_payment_cryptography.types.import_as2805_key_cryptogram.serialize_aws_json_1_0(
                value["As2805KeyCryptogram"]
            )
        }
    else:
        raise SerializationError("ImportKeyMaterial: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ImportKeyMaterial:
    if "RootCertificatePublicKey" in data:
        import capo_payment_cryptography.types.root_certificate_public_key

        return {
            "RootCertificatePublicKey": capo_payment_cryptography.types.root_certificate_public_key.deserialize_aws_json_1_0(
                data["RootCertificatePublicKey"]
            )
        }
    elif "TrustedCertificatePublicKey" in data:
        import capo_payment_cryptography.types.trusted_certificate_public_key

        return {
            "TrustedCertificatePublicKey": capo_payment_cryptography.types.trusted_certificate_public_key.deserialize_aws_json_1_0(
                data["TrustedCertificatePublicKey"]
            )
        }
    elif "Tr31KeyBlock" in data:
        import capo_payment_cryptography.types.import_tr31_key_block

        return {
            "Tr31KeyBlock": capo_payment_cryptography.types.import_tr31_key_block.deserialize_aws_json_1_0(
                data["Tr31KeyBlock"]
            )
        }
    elif "Tr34KeyBlock" in data:
        import capo_payment_cryptography.types.import_tr34_key_block

        return {
            "Tr34KeyBlock": capo_payment_cryptography.types.import_tr34_key_block.deserialize_aws_json_1_0(
                data["Tr34KeyBlock"]
            )
        }
    elif "KeyCryptogram" in data:
        import capo_payment_cryptography.types.import_key_cryptogram

        return {
            "KeyCryptogram": capo_payment_cryptography.types.import_key_cryptogram.deserialize_aws_json_1_0(
                data["KeyCryptogram"]
            )
        }
    elif "DiffieHellmanTr31KeyBlock" in data:
        import capo_payment_cryptography.types.import_diffie_hellman_tr31_key_block

        return {
            "DiffieHellmanTr31KeyBlock": capo_payment_cryptography.types.import_diffie_hellman_tr31_key_block.deserialize_aws_json_1_0(
                data["DiffieHellmanTr31KeyBlock"]
            )
        }
    elif "As2805KeyCryptogram" in data:
        import capo_payment_cryptography.types.import_as2805_key_cryptogram

        return {
            "As2805KeyCryptogram": capo_payment_cryptography.types.import_as2805_key_cryptogram.deserialize_aws_json_1_0(
                data["As2805KeyCryptogram"]
            )
        }
    else:
        raise DeserializationError("ImportKeyMaterial: no recognized variant key")
