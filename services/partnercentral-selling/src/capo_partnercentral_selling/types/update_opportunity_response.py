"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#UpdateOpportunityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.opportunity_identifier


class UpdateOpportunityResponse(TypedDict, closed=True):
    id: "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    """<p>Read-only, system generated <code>Opportunity</code> unique identifier.</p>"""
    last_modified_date: "capo_partnercentral_selling.types.date_time.DateTime"
    """<p> <code>DateTime</code> when the opportunity was last modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateOpportunityResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_partnercentral_selling.types.date_time

    out["LastModifiedDate"] = (
        capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
            value["last_modified_date"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateOpportunityResponse:
    out: UpdateOpportunityResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateOpportunityResponse.id required")
    if "LastModifiedDate" in data:
        import capo_partnercentral_selling.types.date_time

        out["last_modified_date"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["LastModifiedDate"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateOpportunityResponse.last_modified_date required"
        )
    return out
