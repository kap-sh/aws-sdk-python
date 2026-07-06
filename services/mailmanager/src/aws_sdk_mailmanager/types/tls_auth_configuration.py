"""Generated from Smithy shape ``com.amazonaws.mailmanager#TlsAuthConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.trust_store


class TlsAuthConfiguration(TypedDict, closed=True):
    trust_store: NotRequired["aws_sdk_mailmanager.types.trust_store.TrustStore"]
    """<p>The trust store configuration for mutual TLS authentication.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TlsAuthConfiguration) -> dict:
    out: dict = {}
    if "trust_store" in value:
        import aws_sdk_mailmanager.types.trust_store

        out["TrustStore"] = (
            aws_sdk_mailmanager.types.trust_store.serialize_aws_json_1_0(
                value["trust_store"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TlsAuthConfiguration:
    out: TlsAuthConfiguration = {}  # type: ignore[typeddict-item]
    if "TrustStore" in data:
        import aws_sdk_mailmanager.types.trust_store

        out["trust_store"] = (
            aws_sdk_mailmanager.types.trust_store.deserialize_aws_json_1_0(
                data["TrustStore"]
            )
        )
    return out
