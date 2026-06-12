"""Generated from Smithy shape ``com.amazonaws.detective#UpdateOrganizationConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_detective.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_detective.types.boolean
    import aws_sdk_detective.types.graph_arn


class UpdateOrganizationConfigurationRequest(TypedDict):
    graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the organization behavior graph.</p>"""
    auto_enable: "aws_sdk_detective.types.boolean.Boolean"
    """<p>Indicates whether to automatically enable new organization accounts as member accounts in the organization behavior graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOrganizationConfigurationRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    out["AutoEnable"] = value.get("auto_enable", False)
    return out


def deserialize_json(data: dict) -> UpdateOrganizationConfigurationRequest:
    out: UpdateOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    else:
        raise DeserializationError(
            "UpdateOrganizationConfigurationRequest.graph_arn required"
        )
    if "AutoEnable" in data:
        out["auto_enable"] = data["AutoEnable"]
    else:
        out["auto_enable"] = False
    return out
