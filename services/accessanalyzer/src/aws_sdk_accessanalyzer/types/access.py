"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#Access``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.actions_list
    import aws_sdk_accessanalyzer.types.resources_list


class Access(TypedDict):
    actions: "aws_sdk_accessanalyzer.types.actions_list.ActionsList"
    """<p>A list of actions for the access permissions. Any strings that can be used as an action in an IAM policy can be used in the list of actions to check.</p>"""
    resources: "aws_sdk_accessanalyzer.types.resources_list.ResourcesList"
    """<p>A list of resources for the access permissions. Any strings that can be used as an Amazon Resource Name (ARN) in an IAM policy can be used in the list of resources to check. You can only use a wildcard in the portion of the ARN that specifies the resource ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Access) -> dict:
    out: dict = {}
    import aws_sdk_accessanalyzer.types.actions_list

    out["actions"] = aws_sdk_accessanalyzer.types.actions_list.serialize_json(
        value.get("actions", [])
    )
    import aws_sdk_accessanalyzer.types.resources_list

    out["resources"] = aws_sdk_accessanalyzer.types.resources_list.serialize_json(
        value.get("resources", [])
    )
    return out


def deserialize_json(data: dict) -> Access:
    out: Access = {}  # type: ignore[typeddict-item]
    if "actions" in data:
        import aws_sdk_accessanalyzer.types.actions_list

        out["actions"] = aws_sdk_accessanalyzer.types.actions_list.deserialize_json(
            data["actions"]
        )
    else:
        out["actions"] = []
    if "resources" in data:
        import aws_sdk_accessanalyzer.types.resources_list

        out["resources"] = aws_sdk_accessanalyzer.types.resources_list.deserialize_json(
            data["resources"]
        )
    else:
        out["resources"] = []
    return out
