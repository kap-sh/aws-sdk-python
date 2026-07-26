"""Generated from Smithy shape ``com.amazonaws.firehose#InputFormatConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.deserializer


class InputFormatConfiguration(TypedDict, closed=True):
    deserializer: NotRequired["capo_firehose.types.deserializer.Deserializer"]
    """<p>Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputFormatConfiguration) -> dict:
    out: dict = {}
    if "deserializer" in value:
        import capo_firehose.types.deserializer

        out["Deserializer"] = capo_firehose.types.deserializer.serialize_aws_json_1_1(
            value["deserializer"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InputFormatConfiguration:
    out: InputFormatConfiguration = {}  # type: ignore[typeddict-item]
    if "Deserializer" in data:
        import capo_firehose.types.deserializer

        out["deserializer"] = capo_firehose.types.deserializer.deserialize_aws_json_1_1(
            data["Deserializer"]
        )
    return out
