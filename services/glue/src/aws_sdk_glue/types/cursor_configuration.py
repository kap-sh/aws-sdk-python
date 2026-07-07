"""Generated from Smithy shape ``com.amazonaws.glue#CursorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.extracted_parameter


class CursorConfiguration(TypedDict, closed=True):
    next_page: "aws_sdk_glue.types.extracted_parameter.ExtractedParameter"
    """<p>The parameter name or JSON path that contains the cursor or token for retrieving the next page of results.</p>"""
    limit_parameter: NotRequired[
        "aws_sdk_glue.types.extracted_parameter.ExtractedParameter"
    ]
    """<p>The parameter name used to specify the maximum number of results to return per page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CursorConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.extracted_parameter

    out["NextPage"] = aws_sdk_glue.types.extracted_parameter.serialize_aws_json_1_1(
        value["next_page"]
    )
    if "limit_parameter" in value:
        import aws_sdk_glue.types.extracted_parameter

        out["LimitParameter"] = (
            aws_sdk_glue.types.extracted_parameter.serialize_aws_json_1_1(
                value["limit_parameter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CursorConfiguration:
    out: CursorConfiguration = {}  # type: ignore[typeddict-item]
    if "NextPage" in data:
        import aws_sdk_glue.types.extracted_parameter

        out["next_page"] = (
            aws_sdk_glue.types.extracted_parameter.deserialize_aws_json_1_1(
                data["NextPage"]
            )
        )
    else:
        raise DeserializationError("CursorConfiguration.next_page required")
    if "LimitParameter" in data:
        import aws_sdk_glue.types.extracted_parameter

        out["limit_parameter"] = (
            aws_sdk_glue.types.extracted_parameter.deserialize_aws_json_1_1(
                data["LimitParameter"]
            )
        )
    return out
