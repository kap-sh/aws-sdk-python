"""Generated from Smithy shape ``com.amazonaws.glue#OffsetConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.extracted_parameter


class OffsetConfiguration(TypedDict):
    offset_parameter: "aws_sdk_glue.types.extracted_parameter.ExtractedParameter"
    """<p>The parameter name used to specify the starting position or offset for retrieving results.</p>"""
    limit_parameter: "aws_sdk_glue.types.extracted_parameter.ExtractedParameter"
    """<p>The parameter name used to specify the maximum number of results to return per page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OffsetConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.extracted_parameter

    out["OffsetParameter"] = (
        aws_sdk_glue.types.extracted_parameter.serialize_aws_json_1_1(
            value["offset_parameter"]
        )
    )
    import aws_sdk_glue.types.extracted_parameter

    out["LimitParameter"] = (
        aws_sdk_glue.types.extracted_parameter.serialize_aws_json_1_1(
            value["limit_parameter"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OffsetConfiguration:
    out: OffsetConfiguration = {}  # type: ignore[typeddict-item]
    if "OffsetParameter" in data:
        import aws_sdk_glue.types.extracted_parameter

        out["offset_parameter"] = (
            aws_sdk_glue.types.extracted_parameter.deserialize_aws_json_1_1(
                data["OffsetParameter"]
            )
        )
    else:
        raise DeserializationError("OffsetConfiguration.offset_parameter required")
    if "LimitParameter" in data:
        import aws_sdk_glue.types.extracted_parameter

        out["limit_parameter"] = (
            aws_sdk_glue.types.extracted_parameter.deserialize_aws_json_1_1(
                data["LimitParameter"]
            )
        )
    else:
        raise DeserializationError("OffsetConfiguration.limit_parameter required")
    return out
