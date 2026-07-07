"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CategoricalValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.integer
    import aws_sdk_lookoutequipment.types.statistical_issue_status


class CategoricalValues(TypedDict, closed=True):
    status: (
        "aws_sdk_lookoutequipment.types.statistical_issue_status.StatisticalIssueStatus"
    )
    """<p> Indicates whether there is a potential data issue related to categorical values. </p>"""
    number_of_category: NotRequired["aws_sdk_lookoutequipment.types.integer.Integer"]
    """<p> Indicates the number of categories in the data. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CategoricalValues) -> dict:
    out: dict = {}
    import aws_sdk_lookoutequipment.types.statistical_issue_status

    out["Status"] = (
        aws_sdk_lookoutequipment.types.statistical_issue_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "number_of_category" in value:
        out["NumberOfCategory"] = value["number_of_category"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CategoricalValues:
    out: CategoricalValues = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.statistical_issue_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.statistical_issue_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("CategoricalValues.status required")
    if "NumberOfCategory" in data:
        out["number_of_category"] = data["NumberOfCategory"]
    return out
