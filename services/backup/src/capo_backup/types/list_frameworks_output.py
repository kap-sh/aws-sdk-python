"""Generated from Smithy shape ``com.amazonaws.backup#ListFrameworksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.framework_list
    import capo_backup.types.string


class ListFrameworksOutput(TypedDict, closed=True):
    frameworks: NotRequired["capo_backup.types.framework_list.FrameworkList"]
    """<p>The frameworks with details for each framework, including the framework name, Amazon Resource Name (ARN), description, number of controls, creation time, and deployment status.</p>"""
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFrameworksOutput) -> dict:
    out: dict = {}
    if "frameworks" in value:
        import capo_backup.types.framework_list

        out["Frameworks"] = capo_backup.types.framework_list.serialize_json(
            value["frameworks"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFrameworksOutput:
    out: ListFrameworksOutput = {}  # type: ignore[typeddict-item]
    if "Frameworks" in data:
        import capo_backup.types.framework_list

        out["frameworks"] = capo_backup.types.framework_list.deserialize_json(
            data["Frameworks"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
