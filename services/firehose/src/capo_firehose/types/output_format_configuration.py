"""Generated from Smithy shape ``com.amazonaws.firehose#OutputFormatConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.serializer


class OutputFormatConfiguration(TypedDict, closed=True):
    serializer: NotRequired["capo_firehose.types.serializer.Serializer"]
    """<p>Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. If both are non-null, the server rejects the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputFormatConfiguration) -> dict:
    out: dict = {}
    if "serializer" in value:
        import capo_firehose.types.serializer

        out["Serializer"] = capo_firehose.types.serializer.serialize_aws_json_1_1(
            value["serializer"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputFormatConfiguration:
    out: OutputFormatConfiguration = {}  # type: ignore[typeddict-item]
    if "Serializer" in data:
        import capo_firehose.types.serializer

        out["serializer"] = capo_firehose.types.serializer.deserialize_aws_json_1_1(
            data["Serializer"]
        )
    return out
