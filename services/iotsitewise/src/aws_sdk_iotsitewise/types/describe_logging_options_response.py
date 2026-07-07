"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeLoggingOptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.logging_options


class DescribeLoggingOptionsResponse(TypedDict, closed=True):
    logging_options: "aws_sdk_iotsitewise.types.logging_options.LoggingOptions"
    """<p>The current logging options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeLoggingOptionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.logging_options

    out["loggingOptions"] = aws_sdk_iotsitewise.types.logging_options.serialize_json(
        value["logging_options"]
    )
    return out


def deserialize_json(data: dict) -> DescribeLoggingOptionsResponse:
    out: DescribeLoggingOptionsResponse = {}  # type: ignore[typeddict-item]
    if "loggingOptions" in data:
        import aws_sdk_iotsitewise.types.logging_options

        out["logging_options"] = (
            aws_sdk_iotsitewise.types.logging_options.deserialize_json(
                data["loggingOptions"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeLoggingOptionsResponse.logging_options required"
        )
    return out
