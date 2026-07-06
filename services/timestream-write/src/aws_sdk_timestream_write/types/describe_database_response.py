"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DescribeDatabaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.database


class DescribeDatabaseResponse(TypedDict, closed=True):
    database: NotRequired["aws_sdk_timestream_write.types.database.Database"]
    """<p>The name of the Timestream table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeDatabaseResponse) -> dict:
    out: dict = {}
    if "database" in value:
        import aws_sdk_timestream_write.types.database

        out["Database"] = (
            aws_sdk_timestream_write.types.database.serialize_aws_json_1_0(
                value["database"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeDatabaseResponse:
    out: DescribeDatabaseResponse = {}  # type: ignore[typeddict-item]
    if "Database" in data:
        import aws_sdk_timestream_write.types.database

        out["database"] = (
            aws_sdk_timestream_write.types.database.deserialize_aws_json_1_0(
                data["Database"]
            )
        )
    return out
