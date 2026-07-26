"""Generated from Smithy shape ``com.amazonaws.lightsail#RenewalSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.domain_validation_record_list
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.renewal_status
    import capo_lightsail.types.renewal_status_reason


class RenewalSummary(TypedDict, closed=True):
    domain_validation_records: NotRequired[
        "capo_lightsail.types.domain_validation_record_list.DomainValidationRecordList"
    ]
    """<p>An array of objects that describe the domain validation records of the certificate.</p>"""
    renewal_status: NotRequired["capo_lightsail.types.renewal_status.RenewalStatus"]
    """<p>The renewal status of the certificate.</p> <p>The following renewal status are possible:</p> <ul> <li> <p> <b> <code>PendingAutoRenewal</code> </b> - Lightsail is attempting to automatically validate the domain names of the certificate. No further action is required. </p> </li> <li> <p> <b> <code>PendingValidation</code> </b> - Lightsail couldn't automatically validate one or more domain names of the certificate. You must take action to validate these domain names or the certificate won't be renewed. Check to make sure your certificate's domain validation records exist in your domain's DNS, and that your certificate remains in use.</p> </li> <li> <p> <b> <code>Success</code> </b> - All domain names in the certificate are validated, and Lightsail renewed the certificate. No further action is required. </p> </li> <li> <p> <b> <code>Failed</code> </b> - One or more domain names were not validated before the certificate expired, and Lightsail did not renew the certificate. You can request a new certificate using the <code>CreateCertificate</code> action.</p> </li> </ul>"""
    renewal_status_reason: NotRequired[
        "capo_lightsail.types.renewal_status_reason.RenewalStatusReason"
    ]
    """<p>The reason for the renewal status of the certificate.</p>"""
    updated_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the certificate was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenewalSummary) -> dict:
    out: dict = {}
    if "domain_validation_records" in value:
        import capo_lightsail.types.domain_validation_record_list

        out["domainValidationRecords"] = (
            capo_lightsail.types.domain_validation_record_list.serialize_aws_json_1_1(
                value["domain_validation_records"]
            )
        )
    if "renewal_status" in value:
        import capo_lightsail.types.renewal_status

        out["renewalStatus"] = (
            capo_lightsail.types.renewal_status.serialize_aws_json_1_1(
                value["renewal_status"]
            )
        )
    if "renewal_status_reason" in value:
        out["renewalStatusReason"] = value["renewal_status_reason"]
    if "updated_at" in value:
        import capo_lightsail.types.iso_date

        out["updatedAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RenewalSummary:
    out: RenewalSummary = {}  # type: ignore[typeddict-item]
    if "domainValidationRecords" in data:
        import capo_lightsail.types.domain_validation_record_list

        out["domain_validation_records"] = (
            capo_lightsail.types.domain_validation_record_list.deserialize_aws_json_1_1(
                data["domainValidationRecords"]
            )
        )
    if "renewalStatus" in data:
        import capo_lightsail.types.renewal_status

        out["renewal_status"] = (
            capo_lightsail.types.renewal_status.deserialize_aws_json_1_1(
                data["renewalStatus"]
            )
        )
    if "renewalStatusReason" in data:
        out["renewal_status_reason"] = data["renewalStatusReason"]
    if "updatedAt" in data:
        import capo_lightsail.types.iso_date

        out["updated_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    return out
