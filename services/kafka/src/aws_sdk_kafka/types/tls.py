"""Generated from Smithy shape ``com.amazonaws.kafka#Tls``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__boolean
    import aws_sdk_kafka.types.__list_of__string


class Tls(TypedDict):
    certificate_authority_arn_list: NotRequired[
        "aws_sdk_kafka.types.__list_of__string.__listOf__string"
    ]
    """<p>List of ACM Certificate Authority ARNs.</p>"""
    enabled: NotRequired["aws_sdk_kafka.types.__boolean.__boolean"]
    """<p>Specifies whether you want to turn on or turn off TLS authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tls) -> dict:
    out: dict = {}
    if "certificate_authority_arn_list" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["certificateAuthorityArnList"] = (
            aws_sdk_kafka.types.__list_of__string.serialize_json(
                value["certificate_authority_arn_list"]
            )
        )
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> Tls:
    out: Tls = {}  # type: ignore[typeddict-item]
    if "certificateAuthorityArnList" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["certificate_authority_arn_list"] = (
            aws_sdk_kafka.types.__list_of__string.deserialize_json(
                data["certificateAuthorityArnList"]
            )
        )
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
