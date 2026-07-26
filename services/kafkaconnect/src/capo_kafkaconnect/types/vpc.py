"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#Vpc``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__list_of__string


class Vpc(TypedDict, closed=True):
    security_groups: NotRequired[
        "capo_kafkaconnect.types.__list_of__string.__listOf__string"
    ]
    """<p>The security groups for the connector.</p>"""
    subnets: "capo_kafkaconnect.types.__list_of__string.__listOf__string"
    """<p>The subnets for the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Vpc) -> dict:
    out: dict = {}
    if "security_groups" in value:
        import capo_kafkaconnect.types.__list_of__string

        out["securityGroups"] = (
            capo_kafkaconnect.types.__list_of__string.serialize_json(
                value["security_groups"]
            )
        )
    import capo_kafkaconnect.types.__list_of__string

    out["subnets"] = capo_kafkaconnect.types.__list_of__string.serialize_json(
        value["subnets"]
    )
    return out


def deserialize_json(data: dict) -> Vpc:
    out: Vpc = {}  # type: ignore[typeddict-item]
    if "securityGroups" in data:
        import capo_kafkaconnect.types.__list_of__string

        out["security_groups"] = (
            capo_kafkaconnect.types.__list_of__string.deserialize_json(
                data["securityGroups"]
            )
        )
    if "subnets" in data:
        import capo_kafkaconnect.types.__list_of__string

        out["subnets"] = capo_kafkaconnect.types.__list_of__string.deserialize_json(
            data["subnets"]
        )
    else:
        raise DeserializationError("Vpc.subnets required")
    return out
