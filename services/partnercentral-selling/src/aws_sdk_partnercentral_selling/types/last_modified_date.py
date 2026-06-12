"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LastModifiedDate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.date_time


class LastModifiedDate(TypedDict):
    after_last_modified_date: NotRequired[
        "aws_sdk_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p>Specifies the date after which the opportunities were modified. Use this filter to retrieve only those opportunities that were modified after a given timestamp.</p>"""
    before_last_modified_date: NotRequired[
        "aws_sdk_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p>Specifies the date before which the opportunities were modified. Use this filter to retrieve only those opportunities that were modified before a given timestamp.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LastModifiedDate) -> dict:
    out: dict = {}
    if "after_last_modified_date" in value:
        import aws_sdk_partnercentral_selling.types.date_time

        out["AfterLastModifiedDate"] = (
            aws_sdk_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["after_last_modified_date"]
            )
        )
    if "before_last_modified_date" in value:
        import aws_sdk_partnercentral_selling.types.date_time

        out["BeforeLastModifiedDate"] = (
            aws_sdk_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["before_last_modified_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LastModifiedDate:
    out: LastModifiedDate = {}  # type: ignore[typeddict-item]
    if "AfterLastModifiedDate" in data:
        import aws_sdk_partnercentral_selling.types.date_time

        out["after_last_modified_date"] = (
            aws_sdk_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["AfterLastModifiedDate"]
            )
        )
    if "BeforeLastModifiedDate" in data:
        import aws_sdk_partnercentral_selling.types.date_time

        out["before_last_modified_date"] = (
            aws_sdk_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["BeforeLastModifiedDate"]
            )
        )
    return out
