"""Generated from Smithy shape ``com.amazonaws.support#DescribeCreateCaseOptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_support.types.communication_type_options_list
    import aws_sdk_support.types.validated_language_availability


class DescribeCreateCaseOptionsResponse(TypedDict, closed=True):
    language_availability: NotRequired[
        "aws_sdk_support.types.validated_language_availability.ValidatedLanguageAvailability"
    ]
    """<p>Language availability can be any of the following:</p> <ul> <li> <p> available </p> </li> <li> <p> best_effort </p> </li> <li> <p> unavailable </p> </li> </ul>"""
    communication_types: NotRequired[
        "aws_sdk_support.types.communication_type_options_list.CommunicationTypeOptionsList"
    ]
    """<p> A JSON-formatted array that contains the available communication type options, along with the available support timeframes for the given inputs. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCreateCaseOptionsResponse) -> dict:
    out: dict = {}
    if "language_availability" in value:
        out["languageAvailability"] = value["language_availability"]
    if "communication_types" in value:
        import aws_sdk_support.types.communication_type_options_list

        out["communicationTypes"] = (
            aws_sdk_support.types.communication_type_options_list.serialize_aws_json_1_1(
                value["communication_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCreateCaseOptionsResponse:
    out: DescribeCreateCaseOptionsResponse = {}  # type: ignore[typeddict-item]
    if "languageAvailability" in data:
        out["language_availability"] = data["languageAvailability"]
    if "communicationTypes" in data:
        import aws_sdk_support.types.communication_type_options_list

        out["communication_types"] = (
            aws_sdk_support.types.communication_type_options_list.deserialize_aws_json_1_1(
                data["communicationTypes"]
            )
        )
    return out
