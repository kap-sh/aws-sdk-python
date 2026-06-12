"""Generated from Smithy shape ``com.amazonaws.glue#ListBlueprintsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.blueprint_names
    import aws_sdk_glue.types.generic_string


class ListBlueprintsResponse(TypedDict):
    blueprints: NotRequired["aws_sdk_glue.types.blueprint_names.BlueprintNames"]
    """<p>List of names of blueprints in the account.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if not all blueprint names have been returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBlueprintsResponse) -> dict:
    out: dict = {}
    if "blueprints" in value:
        import aws_sdk_glue.types.blueprint_names

        out["Blueprints"] = aws_sdk_glue.types.blueprint_names.serialize_aws_json_1_1(
            value["blueprints"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBlueprintsResponse:
    out: ListBlueprintsResponse = {}  # type: ignore[typeddict-item]
    if "Blueprints" in data:
        import aws_sdk_glue.types.blueprint_names

        out["blueprints"] = aws_sdk_glue.types.blueprint_names.deserialize_aws_json_1_1(
            data["Blueprints"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
