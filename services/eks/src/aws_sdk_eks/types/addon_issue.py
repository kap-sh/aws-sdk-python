"""Generated from Smithy shape ``com.amazonaws.eks#AddonIssue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.addon_issue_code
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list


class AddonIssue(TypedDict, closed=True):
    code: NotRequired["aws_sdk_eks.types.addon_issue_code.AddonIssueCode"]
    """<p>A code that describes the type of issue.</p>"""
    message: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>A message that provides details about the issue and what might cause it.</p>"""
    resource_ids: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>The resource IDs of the issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddonIssue) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_eks.types.addon_issue_code

        out["code"] = aws_sdk_eks.types.addon_issue_code.serialize_json(value["code"])
    if "message" in value:
        out["message"] = value["message"]
    if "resource_ids" in value:
        import aws_sdk_eks.types.string_list

        out["resourceIds"] = aws_sdk_eks.types.string_list.serialize_json(
            value["resource_ids"]
        )
    return out


def deserialize_json(data: dict) -> AddonIssue:
    out: AddonIssue = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import aws_sdk_eks.types.addon_issue_code

        out["code"] = aws_sdk_eks.types.addon_issue_code.deserialize_json(data["code"])
    if "message" in data:
        out["message"] = data["message"]
    if "resourceIds" in data:
        import aws_sdk_eks.types.string_list

        out["resource_ids"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["resourceIds"]
        )
    return out
