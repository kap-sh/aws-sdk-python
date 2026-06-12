"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeSchemaResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.dataset_schema


class DescribeSchemaResponse(TypedDict):
    schema: NotRequired["aws_sdk_personalize.types.dataset_schema.DatasetSchema"]
    """<p>The requested schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSchemaResponse) -> dict:
    out: dict = {}
    if "schema" in value:
        import aws_sdk_personalize.types.dataset_schema

        out["schema"] = aws_sdk_personalize.types.dataset_schema.serialize_aws_json_1_1(
            value["schema"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSchemaResponse:
    out: DescribeSchemaResponse = {}  # type: ignore[typeddict-item]
    if "schema" in data:
        import aws_sdk_personalize.types.dataset_schema

        out["schema"] = (
            aws_sdk_personalize.types.dataset_schema.deserialize_aws_json_1_1(
                data["schema"]
            )
        )
    return out
