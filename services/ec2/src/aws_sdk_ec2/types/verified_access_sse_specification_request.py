"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessSseSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.kms_key_arn


class VerifiedAccessSseSpecificationRequest(TypedDict, closed=True):
    customer_managed_key_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Enable or disable the use of customer managed KMS keys for server side encryption. </p> <p>Valid values: <code>True</code> | <code>False</code> </p>"""
    kms_key_arn: NotRequired["aws_sdk_ec2.types.kms_key_arn.KmsKeyArn"]
    """<p> The ARN of the KMS key. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessSseSpecificationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "customer_managed_key_enabled" in value:
        pairs.append(
            (
                f"{prefix}.CustomerManagedKeyEnabled",
                "true" if value["customer_managed_key_enabled"] else "false",
            )
        )
    if "kms_key_arn" in value:
        pairs.append((f"{prefix}.KmsKeyArn", str(value["kms_key_arn"])))


def deserialize_ec2_query(el: Element) -> VerifiedAccessSseSpecificationRequest:
    out: VerifiedAccessSseSpecificationRequest = {}  # type: ignore[typeddict-item]
    child_customer_managed_key_enabled = el.find("CustomerManagedKeyEnabled")
    if child_customer_managed_key_enabled is not None:
        out["customer_managed_key_enabled"] = (
            child_customer_managed_key_enabled.text or ""
        ).lower() == "true"
    child_kms_key_arn = el.find("KmsKeyArn")
    if child_kms_key_arn is not None:
        out["kms_key_arn"] = str(child_kms_key_arn.text or "")
    return out
