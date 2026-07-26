"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LastModifiedDate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date_time


class LastModifiedDate(TypedDict, closed=True):
    after_last_modified_date: NotRequired[
        "capo_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p>Specifies the date after which the opportunities were modified. Use this filter to retrieve only those opportunities that were modified after a given timestamp.</p>"""
    before_last_modified_date: NotRequired[
        "capo_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p>Specifies the date before which the opportunities were modified. Use this filter to retrieve only those opportunities that were modified before a given timestamp.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LastModifiedDate) -> dict:
    out: dict = {}
    if "after_last_modified_date" in value:
        import capo_partnercentral_selling.types.date_time

        out["AfterLastModifiedDate"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["after_last_modified_date"]
            )
        )
    if "before_last_modified_date" in value:
        import capo_partnercentral_selling.types.date_time

        out["BeforeLastModifiedDate"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["before_last_modified_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LastModifiedDate:
    out: LastModifiedDate = {}  # type: ignore[typeddict-item]
    if "AfterLastModifiedDate" in data:
        import capo_partnercentral_selling.types.date_time

        out["after_last_modified_date"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["AfterLastModifiedDate"]
            )
        )
    if "BeforeLastModifiedDate" in data:
        import capo_partnercentral_selling.types.date_time

        out["before_last_modified_date"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["BeforeLastModifiedDate"]
            )
        )
    return out
