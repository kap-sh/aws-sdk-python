"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#UpdateEngagementContextPayload``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.customer_projects_context
    import capo_partnercentral_selling.types.update_lead_context


class _UpdateEngagementContextPayload_Lead(TypedDict, closed=True):
    Lead: "capo_partnercentral_selling.types.update_lead_context.UpdateLeadContext"


class _UpdateEngagementContextPayload_CustomerProject(TypedDict, closed=True):
    CustomerProject: "capo_partnercentral_selling.types.customer_projects_context.CustomerProjectsContext"


UpdateEngagementContextPayload: TypeAlias = (
    _UpdateEngagementContextPayload_Lead
    | _UpdateEngagementContextPayload_CustomerProject
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEngagementContextPayload) -> dict:
    if "Lead" in value:
        import capo_partnercentral_selling.types.update_lead_context

        return {
            "Lead": capo_partnercentral_selling.types.update_lead_context.serialize_aws_json_1_0(
                value["Lead"]
            )
        }
    elif "CustomerProject" in value:
        import capo_partnercentral_selling.types.customer_projects_context

        return {
            "CustomerProject": capo_partnercentral_selling.types.customer_projects_context.serialize_aws_json_1_0(
                value["CustomerProject"]
            )
        }
    else:
        raise SerializationError("UpdateEngagementContextPayload: no variant present")


def deserialize_aws_json_1_0(data: dict) -> UpdateEngagementContextPayload:
    if "Lead" in data:
        import capo_partnercentral_selling.types.update_lead_context

        return {
            "Lead": capo_partnercentral_selling.types.update_lead_context.deserialize_aws_json_1_0(
                data["Lead"]
            )
        }
    elif "CustomerProject" in data:
        import capo_partnercentral_selling.types.customer_projects_context

        return {
            "CustomerProject": capo_partnercentral_selling.types.customer_projects_context.deserialize_aws_json_1_0(
                data["CustomerProject"]
            )
        }
    else:
        raise DeserializationError(
            "UpdateEngagementContextPayload: no recognized variant key"
        )
