"""Generated from Smithy shape ``com.amazonaws.glue#ListBlueprintsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.blueprint_names
    import capo_glue.types.generic_string


class ListBlueprintsResponse(TypedDict, closed=True):
    blueprints: NotRequired["capo_glue.types.blueprint_names.BlueprintNames"]
    """<p>List of names of blueprints in the account.</p>"""
    next_token: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if not all blueprint names have been returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBlueprintsResponse) -> dict:
    out: dict = {}
    if "blueprints" in value:
        import capo_glue.types.blueprint_names

        out["Blueprints"] = capo_glue.types.blueprint_names.serialize_aws_json_1_1(
            value["blueprints"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBlueprintsResponse:
    out: ListBlueprintsResponse = {}  # type: ignore[typeddict-item]
    if "Blueprints" in data:
        import capo_glue.types.blueprint_names

        out["blueprints"] = capo_glue.types.blueprint_names.deserialize_aws_json_1_1(
            data["Blueprints"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
