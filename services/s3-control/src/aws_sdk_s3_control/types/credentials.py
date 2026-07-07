"""Generated from Smithy shape ``com.amazonaws.s3control#Credentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.access_key_id
    import aws_sdk_s3_control.types.expiration
    import aws_sdk_s3_control.types.secret_access_key
    import aws_sdk_s3_control.types.session_token


class Credentials(TypedDict, closed=True):
    access_key_id: NotRequired["aws_sdk_s3_control.types.access_key_id.AccessKeyId"]
    """<p>The unique access key ID of the Amazon Web Services STS temporary credential that S3 Access Grants vends to grantees and client applications. </p>"""
    secret_access_key: NotRequired[
        "aws_sdk_s3_control.types.secret_access_key.SecretAccessKey"
    ]
    """<p>The secret access key of the Amazon Web Services STS temporary credential that S3 Access Grants vends to grantees and client applications. </p>"""
    session_token: NotRequired["aws_sdk_s3_control.types.session_token.SessionToken"]
    """<p>The Amazon Web Services STS temporary credential that S3 Access Grants vends to grantees and client applications. </p>"""
    expiration: NotRequired["aws_sdk_s3_control.types.expiration.Expiration"]
    """<p>The expiration date and time of the temporary credential that S3 Access Grants vends to grantees and client applications. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: Credentials, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "access_key_id" in value:
        SubElement(el, "AccessKeyId").text = str(value["access_key_id"])
    if "secret_access_key" in value:
        SubElement(el, "SecretAccessKey").text = str(value["secret_access_key"])
    if "session_token" in value:
        SubElement(el, "SessionToken").text = str(value["session_token"])
    if "expiration" in value:
        import aws_sdk_s3_control.types.expiration

        aws_sdk_s3_control.types.expiration.serialize_xml(
            value["expiration"], el, "Expiration"
        )


def deserialize_xml(el: Element) -> Credentials:
    out: Credentials = {}  # type: ignore[typeddict-item]
    child_access_key_id = el.find("AccessKeyId")
    if child_access_key_id is not None:
        out["access_key_id"] = str(child_access_key_id.text or "")
    child_secret_access_key = el.find("SecretAccessKey")
    if child_secret_access_key is not None:
        out["secret_access_key"] = str(child_secret_access_key.text or "")
    child_session_token = el.find("SessionToken")
    if child_session_token is not None:
        out["session_token"] = str(child_session_token.text or "")
    child_expiration = el.find("Expiration")
    if child_expiration is not None:
        import aws_sdk_s3_control.types.expiration

        out["expiration"] = aws_sdk_s3_control.types.expiration.deserialize_xml(
            child_expiration
        )
    return out
