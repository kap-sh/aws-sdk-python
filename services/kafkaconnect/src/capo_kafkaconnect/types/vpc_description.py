"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#VpcDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__list_of__string


class VpcDescription(TypedDict, closed=True):
    security_groups: NotRequired[
        "capo_kafkaconnect.types.__list_of__string.__listOf__string"
    ]
    """<p>The security groups for the connector.</p>"""
    subnets: NotRequired["capo_kafkaconnect.types.__list_of__string.__listOf__string"]
    """<p>The subnets for the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcDescription) -> dict:
    out: dict = {}
    if "security_groups" in value:
        import capo_kafkaconnect.types.__list_of__string

        out["securityGroups"] = (
            capo_kafkaconnect.types.__list_of__string.serialize_json(
                value["security_groups"]
            )
        )
    if "subnets" in value:
        import capo_kafkaconnect.types.__list_of__string

        out["subnets"] = capo_kafkaconnect.types.__list_of__string.serialize_json(
            value["subnets"]
        )
    return out


def deserialize_json(data: dict) -> VpcDescription:
    out: VpcDescription = {}  # type: ignore[typeddict-item]
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
    return out
