"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ListNotifyCountriesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.notify_country_information_list


class ListNotifyCountriesResult(TypedDict, closed=True):
    notify_countries: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.notify_country_information_list.NotifyCountryInformationList"
    ]
    """<p>An array of NotifyCountryInformation objects that contain the results.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. If this field is empty then there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListNotifyCountriesResult) -> dict:
    out: dict = {}
    if "notify_countries" in value:
        import capo_pinpoint_sms_voice_v2.types.notify_country_information_list

        out["NotifyCountries"] = (
            capo_pinpoint_sms_voice_v2.types.notify_country_information_list.serialize_aws_json_1_0(
                value["notify_countries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListNotifyCountriesResult:
    out: ListNotifyCountriesResult = {}  # type: ignore[typeddict-item]
    if "NotifyCountries" in data:
        import capo_pinpoint_sms_voice_v2.types.notify_country_information_list

        out["notify_countries"] = (
            capo_pinpoint_sms_voice_v2.types.notify_country_information_list.deserialize_aws_json_1_0(
                data["NotifyCountries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
