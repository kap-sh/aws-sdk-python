"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GroupDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.group_definition_type


class GroupDefinition(TypedDict):
    key: "str"
    """<p>The key to use for grouping cost and usage data.</p>"""
    type: "aws_sdk_bcm_dashboards.types.group_definition_type.GroupDefinitionType"
    """<p>The type of grouping to apply.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GroupDefinition) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import aws_sdk_bcm_dashboards.types.group_definition_type

    out["type"] = (
        aws_sdk_bcm_dashboards.types.group_definition_type.serialize_aws_json_1_0(
            value.get("type", "DIMENSION")
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GroupDefinition:
    out: GroupDefinition = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("GroupDefinition.key required")
    if "type" in data:
        import aws_sdk_bcm_dashboards.types.group_definition_type

        out["type"] = (
            aws_sdk_bcm_dashboards.types.group_definition_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    else:
        out["type"] = "DIMENSION"
    return out
