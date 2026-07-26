"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementContextPayload``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.customer_projects_context
    import capo_partnercentral_selling.types.lead_context


class _EngagementContextPayload_CustomerProject(TypedDict, closed=True):
    CustomerProject: "capo_partnercentral_selling.types.customer_projects_context.CustomerProjectsContext"


class _EngagementContextPayload_Lead(TypedDict, closed=True):
    Lead: "capo_partnercentral_selling.types.lead_context.LeadContext"


EngagementContextPayload: TypeAlias = (
    _EngagementContextPayload_CustomerProject | _EngagementContextPayload_Lead
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementContextPayload) -> dict:
    if "CustomerProject" in value:
        import capo_partnercentral_selling.types.customer_projects_context

        return {
            "CustomerProject": capo_partnercentral_selling.types.customer_projects_context.serialize_aws_json_1_0(
                value["CustomerProject"]
            )
        }
    elif "Lead" in value:
        import capo_partnercentral_selling.types.lead_context

        return {
            "Lead": capo_partnercentral_selling.types.lead_context.serialize_aws_json_1_0(
                value["Lead"]
            )
        }
    else:
        raise SerializationError("EngagementContextPayload: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EngagementContextPayload:
    if "CustomerProject" in data:
        import capo_partnercentral_selling.types.customer_projects_context

        return {
            "CustomerProject": capo_partnercentral_selling.types.customer_projects_context.deserialize_aws_json_1_0(
                data["CustomerProject"]
            )
        }
    elif "Lead" in data:
        import capo_partnercentral_selling.types.lead_context

        return {
            "Lead": capo_partnercentral_selling.types.lead_context.deserialize_aws_json_1_0(
                data["Lead"]
            )
        }
    else:
        raise DeserializationError(
            "EngagementContextPayload: no recognized variant key"
        )
