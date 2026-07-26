"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.domain_id
    import capo_sagemaker.types.retention_policy


class DeleteDomainRequest(TypedDict, closed=True):
    domain_id: NotRequired["capo_sagemaker.types.domain_id.DomainId"]
    """<p>The domain ID.</p>"""
    retention_policy: NotRequired[
        "capo_sagemaker.types.retention_policy.RetentionPolicy"
    ]
    """<p>The retention policy for this domain, which specifies whether resources will be retained after the Domain is deleted. By default, all resources are retained (not automatically deleted). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDomainRequest) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "retention_policy" in value:
        import capo_sagemaker.types.retention_policy

        out["RetentionPolicy"] = (
            capo_sagemaker.types.retention_policy.serialize_aws_json_1_1(
                value["retention_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDomainRequest:
    out: DeleteDomainRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "RetentionPolicy" in data:
        import capo_sagemaker.types.retention_policy

        out["retention_policy"] = (
            capo_sagemaker.types.retention_policy.deserialize_aws_json_1_1(
                data["RetentionPolicy"]
            )
        )
    return out
