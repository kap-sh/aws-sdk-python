"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#UnableToDetectSchemaException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.error_message
    import aws_sdk_kinesis_analytics.types.processed_input_records
    import aws_sdk_kinesis_analytics.types.raw_input_records


class UnableToDetectSchemaException_(TypedDict):
    message: NotRequired["aws_sdk_kinesis_analytics.types.error_message.ErrorMessage"]
    raw_input_records: NotRequired[
        "aws_sdk_kinesis_analytics.types.raw_input_records.RawInputRecords"
    ]
    processed_input_records: NotRequired[
        "aws_sdk_kinesis_analytics.types.processed_input_records.ProcessedInputRecords"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnableToDetectSchemaException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "raw_input_records" in value:
        import aws_sdk_kinesis_analytics.types.raw_input_records

        out["RawInputRecords"] = (
            aws_sdk_kinesis_analytics.types.raw_input_records.serialize_aws_json_1_1(
                value["raw_input_records"]
            )
        )
    if "processed_input_records" in value:
        import aws_sdk_kinesis_analytics.types.processed_input_records

        out["ProcessedInputRecords"] = (
            aws_sdk_kinesis_analytics.types.processed_input_records.serialize_aws_json_1_1(
                value["processed_input_records"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnableToDetectSchemaException_:
    out: UnableToDetectSchemaException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "RawInputRecords" in data:
        import aws_sdk_kinesis_analytics.types.raw_input_records

        out["raw_input_records"] = (
            aws_sdk_kinesis_analytics.types.raw_input_records.deserialize_aws_json_1_1(
                data["RawInputRecords"]
            )
        )
    if "ProcessedInputRecords" in data:
        import aws_sdk_kinesis_analytics.types.processed_input_records

        out["processed_input_records"] = (
            aws_sdk_kinesis_analytics.types.processed_input_records.deserialize_aws_json_1_1(
                data["ProcessedInputRecords"]
            )
        )
    return out


class UnableToDetectSchemaException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisanalytics#UnableToDetectSchemaException``."""

    code: str | None = "UnableToDetectSchemaException"

    def __init__(self, data: UnableToDetectSchemaException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnableToDetectSchemaException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnableToDetectSchemaException":
        return cls(deserialize_aws_json_1_1(data))
