"""Generated from Smithy shape ``com.amazonaws.servicequotas#DisassociateServiceQuotaTemplateRequest``."""

from typing_extensions import TypedDict


class DisassociateServiceQuotaTemplateRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateServiceQuotaTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateServiceQuotaTemplateRequest:
    out: DisassociateServiceQuotaTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
