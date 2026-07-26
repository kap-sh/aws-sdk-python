"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreatedDateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date_time


class CreatedDateFilter(TypedDict, closed=True):
    after_created_date: NotRequired[
        "capo_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p>Filter opportunities created after this date.</p>"""
    before_created_date: NotRequired[
        "capo_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p>Filter opportunities created before this date.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatedDateFilter) -> dict:
    out: dict = {}
    if "after_created_date" in value:
        import capo_partnercentral_selling.types.date_time

        out["AfterCreatedDate"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["after_created_date"]
            )
        )
    if "before_created_date" in value:
        import capo_partnercentral_selling.types.date_time

        out["BeforeCreatedDate"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["before_created_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatedDateFilter:
    out: CreatedDateFilter = {}  # type: ignore[typeddict-item]
    if "AfterCreatedDate" in data:
        import capo_partnercentral_selling.types.date_time

        out["after_created_date"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["AfterCreatedDate"]
            )
        )
    if "BeforeCreatedDate" in data:
        import capo_partnercentral_selling.types.date_time

        out["before_created_date"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["BeforeCreatedDate"]
            )
        )
    return out
