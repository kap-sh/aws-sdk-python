"""Generated from Smithy shape ``com.amazonaws.firehose#OutputFormatConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.serializer


class OutputFormatConfiguration(TypedDict):
    serializer: NotRequired["aws_sdk_firehose.types.serializer.Serializer"]
    """<p>Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. If both are non-null, the server rejects the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputFormatConfiguration) -> dict:
    out: dict = {}
    if "serializer" in value:
        import aws_sdk_firehose.types.serializer

        out["Serializer"] = aws_sdk_firehose.types.serializer.serialize_aws_json_1_1(
            value["serializer"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputFormatConfiguration:
    out: OutputFormatConfiguration = {}  # type: ignore[typeddict-item]
    if "Serializer" in data:
        import aws_sdk_firehose.types.serializer

        out["serializer"] = aws_sdk_firehose.types.serializer.deserialize_aws_json_1_1(
            data["Serializer"]
        )
    return out
