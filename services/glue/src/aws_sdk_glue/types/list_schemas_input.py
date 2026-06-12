"""Generated from Smithy shape ``com.amazonaws.glue#ListSchemasInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.max_results_number
    import aws_sdk_glue.types.registry_id
    import aws_sdk_glue.types.schema_registry_token_string


class ListSchemasInput(TypedDict):
    registry_id: NotRequired["aws_sdk_glue.types.registry_id.RegistryId"]
    """<p>A wrapper structure that may contain the registry name and Amazon Resource Name (ARN).</p>"""
    max_results: NotRequired["aws_sdk_glue.types.max_results_number.MaxResultsNumber"]
    """<p>Maximum number of results required per page. If the value is not supplied, this will be defaulted to 25 per page.</p>"""
    next_token: NotRequired[
        "aws_sdk_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
    ]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSchemasInput) -> dict:
    out: dict = {}
    if "registry_id" in value:
        import aws_sdk_glue.types.registry_id

        out["RegistryId"] = aws_sdk_glue.types.registry_id.serialize_aws_json_1_1(
            value["registry_id"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSchemasInput:
    out: ListSchemasInput = {}  # type: ignore[typeddict-item]
    if "RegistryId" in data:
        import aws_sdk_glue.types.registry_id

        out["registry_id"] = aws_sdk_glue.types.registry_id.deserialize_aws_json_1_1(
            data["RegistryId"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
