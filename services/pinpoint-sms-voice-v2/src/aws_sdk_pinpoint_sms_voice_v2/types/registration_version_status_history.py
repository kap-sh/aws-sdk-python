"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationVersionStatusHistory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class RegistrationVersionStatusHistory(TypedDict, closed=True):
    draft_timestamp: "datetime.datetime"
    r"""<p>The time when the registration was in the draft state, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""
    submitted_timestamp: NotRequired["datetime.datetime"]
    r"""<p>The time when the registration was in the submitted state, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""
    aws_reviewing_timestamp: NotRequired["datetime.datetime"]
    r"""<p>The time when the registration was in the AWS reviewing state, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""
    reviewing_timestamp: NotRequired["datetime.datetime"]
    r"""<p>The time when the registration was in the reviewing state, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""
    requires_authentication_timestamp: NotRequired["datetime.datetime"]
    r"""<p>The time when the registration was in the requires authentication state, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""
    approved_timestamp: NotRequired["datetime.datetime"]
    r"""<p>The time when the registration was in the approved state, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""
    discarded_timestamp: NotRequired["datetime.datetime"]
    r"""<p>The time when the registration was in the discarded state, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""
    denied_timestamp: NotRequired["datetime.datetime"]
    r"""<p>The time when the registration was in the denied state, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""
    revoked_timestamp: NotRequired["datetime.datetime"]
    r"""<p>The time when the registration was in the revoked state, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""
    archived_timestamp: NotRequired["datetime.datetime"]
    r"""<p>The time when the registration was in the archived state, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationVersionStatusHistory) -> dict:
    out: dict = {}
    import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["DraftTimestamp"] = (
        aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["draft_timestamp"]
        )
    )
    if "submitted_timestamp" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["SubmittedTimestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["submitted_timestamp"]
            )
        )
    if "aws_reviewing_timestamp" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["AwsReviewingTimestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["aws_reviewing_timestamp"]
            )
        )
    if "reviewing_timestamp" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["ReviewingTimestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["reviewing_timestamp"]
            )
        )
    if "requires_authentication_timestamp" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["RequiresAuthenticationTimestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["requires_authentication_timestamp"]
            )
        )
    if "approved_timestamp" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["ApprovedTimestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["approved_timestamp"]
            )
        )
    if "discarded_timestamp" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["DiscardedTimestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["discarded_timestamp"]
            )
        )
    if "denied_timestamp" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["DeniedTimestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["denied_timestamp"]
            )
        )
    if "revoked_timestamp" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["RevokedTimestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["revoked_timestamp"]
            )
        )
    if "archived_timestamp" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["ArchivedTimestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["archived_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegistrationVersionStatusHistory:
    out: RegistrationVersionStatusHistory = {}  # type: ignore[typeddict-item]
    if "DraftTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["draft_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["DraftTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "RegistrationVersionStatusHistory.draft_timestamp required"
        )
    if "SubmittedTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["submitted_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["SubmittedTimestamp"]
            )
        )
    if "AwsReviewingTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["aws_reviewing_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["AwsReviewingTimestamp"]
            )
        )
    if "ReviewingTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["reviewing_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["ReviewingTimestamp"]
            )
        )
    if "RequiresAuthenticationTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["requires_authentication_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["RequiresAuthenticationTimestamp"]
            )
        )
    if "ApprovedTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["approved_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["ApprovedTimestamp"]
            )
        )
    if "DiscardedTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["discarded_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["DiscardedTimestamp"]
            )
        )
    if "DeniedTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["denied_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["DeniedTimestamp"]
            )
        )
    if "RevokedTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["revoked_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["RevokedTimestamp"]
            )
        )
    if "ArchivedTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["archived_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["ArchivedTimestamp"]
            )
        )
    return out
