"""Generated from Smithy shape ``com.amazonaws.connecthealth#ListDomainsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.domain_summary_list


class ListDomainsOutput(TypedDict):
    domains: "aws_sdk_connecthealth.types.domain_summary_list.DomainSummaryList"
    """<p>List of Domains.</p>"""
    next_token: NotRequired["str"]
    """<p>Token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsOutput) -> dict:
    out: dict = {}
    import aws_sdk_connecthealth.types.domain_summary_list

    out["domains"] = aws_sdk_connecthealth.types.domain_summary_list.serialize_json(
        value["domains"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainsOutput:
    out: ListDomainsOutput = {}  # type: ignore[typeddict-item]
    if "domains" in data:
        import aws_sdk_connecthealth.types.domain_summary_list

        out["domains"] = (
            aws_sdk_connecthealth.types.domain_summary_list.deserialize_json(
                data["domains"]
            )
        )
    else:
        raise DeserializationError("ListDomainsOutput.domains required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
