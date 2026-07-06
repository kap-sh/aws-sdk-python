"""Generated from Smithy shape ``com.amazonaws.servicequotas#AssociateServiceQuotaTemplateRequest``."""

from typing_extensions import TypedDict


class AssociateServiceQuotaTemplateRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateServiceQuotaTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateServiceQuotaTemplateRequest:
    out: AssociateServiceQuotaTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
