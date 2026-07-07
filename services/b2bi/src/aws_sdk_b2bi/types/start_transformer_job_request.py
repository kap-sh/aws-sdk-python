"""Generated from Smithy shape ``com.amazonaws.b2bi#StartTransformerJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.s3_location
    import aws_sdk_b2bi.types.transformer_id


class StartTransformerJobRequest(TypedDict, closed=True):
    input_file: "aws_sdk_b2bi.types.s3_location.S3Location"
    """<p>Specifies the location of the input file for the transformation. The location consists of an Amazon S3 bucket and prefix.</p>"""
    output_location: "aws_sdk_b2bi.types.s3_location.S3Location"
    """<p>Specifies the location of the output file for the transformation. The location consists of an Amazon S3 bucket and prefix.</p>"""
    transformer_id: "aws_sdk_b2bi.types.transformer_id.TransformerId"
    """<p>Specifies the system-assigned unique identifier for the transformer.</p>"""
    client_token: NotRequired["str"]
    """<p>Reserved for future use.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartTransformerJobRequest) -> dict:
    out: dict = {}
    import aws_sdk_b2bi.types.s3_location

    out["inputFile"] = aws_sdk_b2bi.types.s3_location.serialize_aws_json_1_0(
        value["input_file"]
    )
    import aws_sdk_b2bi.types.s3_location

    out["outputLocation"] = aws_sdk_b2bi.types.s3_location.serialize_aws_json_1_0(
        value["output_location"]
    )
    out["transformerId"] = value["transformer_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartTransformerJobRequest:
    out: StartTransformerJobRequest = {}  # type: ignore[typeddict-item]
    if "inputFile" in data:
        import aws_sdk_b2bi.types.s3_location

        out["input_file"] = aws_sdk_b2bi.types.s3_location.deserialize_aws_json_1_0(
            data["inputFile"]
        )
    else:
        raise DeserializationError("StartTransformerJobRequest.input_file required")
    if "outputLocation" in data:
        import aws_sdk_b2bi.types.s3_location

        out["output_location"] = (
            aws_sdk_b2bi.types.s3_location.deserialize_aws_json_1_0(
                data["outputLocation"]
            )
        )
    else:
        raise DeserializationError(
            "StartTransformerJobRequest.output_location required"
        )
    if "transformerId" in data:
        out["transformer_id"] = data["transformerId"]
    else:
        raise DeserializationError("StartTransformerJobRequest.transformer_id required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
