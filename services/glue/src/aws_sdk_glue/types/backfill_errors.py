"""Generated from Smithy shape ``com.amazonaws.glue#BackfillErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.backfill_error

BackfillErrors: TypeAlias = list["aws_sdk_glue.types.backfill_error.BackfillError"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackfillErrors) -> list:
    import aws_sdk_glue.types.backfill_error

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.backfill_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BackfillErrors:
    import aws_sdk_glue.types.backfill_error

    out: BackfillErrors = []
    for item in data:
        out.append(aws_sdk_glue.types.backfill_error.deserialize_aws_json_1_1(item))
    return out
