"""Generated from Smithy shape ``com.amazonaws.servicequotas#GetAssociationForServiceQuotaTemplateRequest``."""

from typing_extensions import TypedDict


class GetAssociationForServiceQuotaTemplateRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAssociationForServiceQuotaTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetAssociationForServiceQuotaTemplateRequest:
    out: GetAssociationForServiceQuotaTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
