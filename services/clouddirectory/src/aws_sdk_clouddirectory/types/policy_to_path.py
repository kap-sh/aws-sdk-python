"""Generated from Smithy shape ``com.amazonaws.clouddirectory#PolicyToPath``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.path_string
    import aws_sdk_clouddirectory.types.policy_attachment_list


class PolicyToPath(TypedDict, closed=True):
    path: NotRequired["aws_sdk_clouddirectory.types.path_string.PathString"]
    """<p>The path that is referenced from the root.</p>"""
    policies: NotRequired[
        "aws_sdk_clouddirectory.types.policy_attachment_list.PolicyAttachmentList"
    ]
    """<p>List of policy objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyToPath) -> dict:
    out: dict = {}
    if "path" in value:
        out["Path"] = value["path"]
    if "policies" in value:
        import aws_sdk_clouddirectory.types.policy_attachment_list

        out["Policies"] = (
            aws_sdk_clouddirectory.types.policy_attachment_list.serialize_json(
                value["policies"]
            )
        )
    return out


def deserialize_json(data: dict) -> PolicyToPath:
    out: PolicyToPath = {}  # type: ignore[typeddict-item]
    if "Path" in data:
        out["path"] = data["Path"]
    if "Policies" in data:
        import aws_sdk_clouddirectory.types.policy_attachment_list

        out["policies"] = (
            aws_sdk_clouddirectory.types.policy_attachment_list.deserialize_json(
                data["Policies"]
            )
        )
    return out
