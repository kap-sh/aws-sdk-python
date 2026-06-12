"""Generated from Smithy shape ``com.amazonaws.sesv2#VerificationInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.soa_record
    import aws_sdk_sesv2.types.timestamp
    import aws_sdk_sesv2.types.verification_error


class VerificationInfo(TypedDict):
    last_checked_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The last time a verification attempt was made for this identity.</p>"""
    last_success_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The last time a successful verification was made for this identity.</p>"""
    error_type: NotRequired["aws_sdk_sesv2.types.verification_error.VerificationError"]
    """<p>Provides the reason for the failure describing why Amazon SES was not able to successfully verify the identity. Below are the possible values: </p> <ul> <li> <p> <code>INVALID_VALUE</code> – Amazon SES was able to find the record, but the value contained within the record was invalid. Ensure you have published the correct values for the record.</p> </li> <li> <p> <code>TYPE_NOT_FOUND</code> – The queried hostname exists but does not have the requested type of DNS record. Ensure that you have published the correct type of DNS record.</p> </li> <li> <p> <code>HOST_NOT_FOUND</code> – The queried hostname does not exist or was not reachable at the time of the request. Ensure that you have published the required DNS record(s). </p> </li> <li> <p> <code>SERVICE_ERROR</code> – A temporary issue is preventing Amazon SES from determining the verification status of the domain.</p> </li> <li> <p> <code>DNS_SERVER_ERROR</code> – The DNS server encountered an issue and was unable to complete the request.</p> </li> <li> <p> <code>REPLICATION_ACCESS_DENIED</code> – The verification failed because the user does not have the required permissions to replicate the DKIM key from the primary region. Ensure you have the necessary permissions in both primary and replica regions. </p> </li> <li> <p> <code>REPLICATION_PRIMARY_NOT_FOUND</code> – The verification failed because no corresponding identity was found in the specified primary region. Ensure the identity exists in the primary region before attempting replication. </p> </li> <li> <p> <code>REPLICATION_PRIMARY_BYO_DKIM_NOT_SUPPORTED</code> – The verification failed because the identity in the primary region is configured with Bring Your Own DKIM (BYODKIM). DKIM key replication is only supported for identities using Easy DKIM. </p> </li> <li> <p> <code>REPLICATION_REPLICA_AS_PRIMARY_NOT_SUPPORTED</code> – The verification failed because the specified primary identity is a replica of another identity, and multi-level replication is not supported; the primary identity must be a non-replica identity. </p> </li> <li> <p> <code>REPLICATION_PRIMARY_INVALID_REGION</code> – The verification failed due to an invalid primary region specified. Ensure you provide a valid Amazon Web Services region where Amazon SES is available and different from the replica region. </p> </li> </ul>"""
    soa_record: NotRequired["aws_sdk_sesv2.types.soa_record.SOARecord"]
    """<p>An object that contains information about the start of authority (SOA) record associated with the identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerificationInfo) -> dict:
    out: dict = {}
    if "last_checked_timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["LastCheckedTimestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["last_checked_timestamp"]
        )
    if "last_success_timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["LastSuccessTimestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["last_success_timestamp"]
        )
    if "error_type" in value:
        import aws_sdk_sesv2.types.verification_error

        out["ErrorType"] = aws_sdk_sesv2.types.verification_error.serialize_json(
            value["error_type"]
        )
    if "soa_record" in value:
        import aws_sdk_sesv2.types.soa_record

        out["SOARecord"] = aws_sdk_sesv2.types.soa_record.serialize_json(
            value["soa_record"]
        )
    return out


def deserialize_json(data: dict) -> VerificationInfo:
    out: VerificationInfo = {}  # type: ignore[typeddict-item]
    if "LastCheckedTimestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["last_checked_timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["LastCheckedTimestamp"]
        )
    if "LastSuccessTimestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["last_success_timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["LastSuccessTimestamp"]
        )
    if "ErrorType" in data:
        import aws_sdk_sesv2.types.verification_error

        out["error_type"] = aws_sdk_sesv2.types.verification_error.deserialize_json(
            data["ErrorType"]
        )
    if "SOARecord" in data:
        import aws_sdk_sesv2.types.soa_record

        out["soa_record"] = aws_sdk_sesv2.types.soa_record.deserialize_json(
            data["SOARecord"]
        )
    return out
