"""Generated from Smithy shape ``com.amazonaws.proton#ListServicesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.next_token
    import capo_proton.types.service_summary_list


class ListServicesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next service in the array of services, after the current requested list of services.</p>"""
    services: "capo_proton.types.service_summary_list.ServiceSummaryList"
    """<p>An array of services with summaries of detail data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServicesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_proton.types.service_summary_list

    out["services"] = capo_proton.types.service_summary_list.serialize_aws_json_1_0(
        value["services"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServicesOutput:
    out: ListServicesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "services" in data:
        import capo_proton.types.service_summary_list

        out["services"] = (
            capo_proton.types.service_summary_list.deserialize_aws_json_1_0(
                data["services"]
            )
        )
    else:
        raise DeserializationError("ListServicesOutput.services required")
    return out
