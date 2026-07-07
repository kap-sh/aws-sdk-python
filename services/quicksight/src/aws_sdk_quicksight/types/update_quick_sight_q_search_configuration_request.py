"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateQuickSightQSearchConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.q_search_status


class UpdateQuickSightQSearchConfigurationRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the Quick Sight Q Search configuration that you want to update.</p>"""
    q_search_status: "aws_sdk_quicksight.types.q_search_status.QSearchStatus"
    """<p>The status of the Quick Sight Q Search configuration that the user wants to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQuickSightQSearchConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.q_search_status

    out["QSearchStatus"] = aws_sdk_quicksight.types.q_search_status.serialize_json(
        value["q_search_status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateQuickSightQSearchConfigurationRequest:
    out: UpdateQuickSightQSearchConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "QSearchStatus" in data:
        import aws_sdk_quicksight.types.q_search_status

        out["q_search_status"] = (
            aws_sdk_quicksight.types.q_search_status.deserialize_json(
                data["QSearchStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateQuickSightQSearchConfigurationRequest.q_search_status required"
        )
    return out
