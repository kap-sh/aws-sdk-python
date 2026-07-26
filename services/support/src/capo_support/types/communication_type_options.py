"""Generated from Smithy shape ``com.amazonaws.support#CommunicationTypeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.dates_without_support_list
    import capo_support.types.supported_hours_list
    import capo_support.types.type


class CommunicationTypeOptions(TypedDict, closed=True):
    type: NotRequired["capo_support.types.type.Type"]
    """<p> A string value indicating the communication type. At the moment the type value can assume one of 3 values at the moment chat, web and call. </p>"""
    supported_hours: NotRequired[
        "capo_support.types.supported_hours_list.SupportedHoursList"
    ]
    """<p> A JSON-formatted list containing time ranges when support is available. </p>"""
    dates_without_support: NotRequired[
        "capo_support.types.dates_without_support_list.DatesWithoutSupportList"
    ]
    """<p> A JSON-formatted list containing date and time ranges for periods without support </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommunicationTypeOptions) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "supported_hours" in value:
        import capo_support.types.supported_hours_list

        out["supportedHours"] = (
            capo_support.types.supported_hours_list.serialize_aws_json_1_1(
                value["supported_hours"]
            )
        )
    if "dates_without_support" in value:
        import capo_support.types.dates_without_support_list

        out["datesWithoutSupport"] = (
            capo_support.types.dates_without_support_list.serialize_aws_json_1_1(
                value["dates_without_support"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CommunicationTypeOptions:
    out: CommunicationTypeOptions = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "supportedHours" in data:
        import capo_support.types.supported_hours_list

        out["supported_hours"] = (
            capo_support.types.supported_hours_list.deserialize_aws_json_1_1(
                data["supportedHours"]
            )
        )
    if "datesWithoutSupport" in data:
        import capo_support.types.dates_without_support_list

        out["dates_without_support"] = (
            capo_support.types.dates_without_support_list.deserialize_aws_json_1_1(
                data["datesWithoutSupport"]
            )
        )
    return out
