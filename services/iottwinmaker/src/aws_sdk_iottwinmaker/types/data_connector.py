"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DataConnector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.boolean
    import aws_sdk_iottwinmaker.types.lambda_function

DataConnector = TypedDict(
    "DataConnector",
    {
        "lambda": NotRequired[
            "aws_sdk_iottwinmaker.types.lambda_function.LambdaFunction"
        ],
        "is_native": NotRequired["aws_sdk_iottwinmaker.types.boolean.Boolean"],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: DataConnector) -> dict:
    out: dict = {}
    if "lambda" in value:
        import aws_sdk_iottwinmaker.types.lambda_function

        out["lambda"] = aws_sdk_iottwinmaker.types.lambda_function.serialize_json(
            value["lambda"]
        )
    if "is_native" in value:
        out["isNative"] = value["is_native"]
    return out


def deserialize_json(data: dict) -> DataConnector:
    out: DataConnector = {}  # type: ignore[typeddict-item]
    if "lambda" in data:
        import aws_sdk_iottwinmaker.types.lambda_function

        out["lambda"] = aws_sdk_iottwinmaker.types.lambda_function.deserialize_json(
            data["lambda"]
        )
    if "isNative" in data:
        out["is_native"] = data["isNative"]
    return out
