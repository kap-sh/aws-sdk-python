"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchGetSecurityControlsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.security_controls
    import aws_sdk_securityhub.types.unprocessed_security_controls


class BatchGetSecurityControlsResponse(TypedDict, closed=True):
    security_controls: NotRequired[
        "aws_sdk_securityhub.types.security_controls.SecurityControls"
    ]
    """<p> An array that returns the identifier, Amazon Resource Name (ARN), and other details about a security control. The same information is returned whether the request includes <code>SecurityControlId</code> or <code>SecurityControlArn</code>. </p>"""
    unprocessed_ids: NotRequired[
        "aws_sdk_securityhub.types.unprocessed_security_controls.UnprocessedSecurityControls"
    ]
    """<p> A security control (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters) for which details cannot be returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSecurityControlsResponse) -> dict:
    out: dict = {}
    if "security_controls" in value:
        import aws_sdk_securityhub.types.security_controls

        out["SecurityControls"] = (
            aws_sdk_securityhub.types.security_controls.serialize_json(
                value["security_controls"]
            )
        )
    if "unprocessed_ids" in value:
        import aws_sdk_securityhub.types.unprocessed_security_controls

        out["UnprocessedIds"] = (
            aws_sdk_securityhub.types.unprocessed_security_controls.serialize_json(
                value["unprocessed_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetSecurityControlsResponse:
    out: BatchGetSecurityControlsResponse = {}  # type: ignore[typeddict-item]
    if "SecurityControls" in data:
        import aws_sdk_securityhub.types.security_controls

        out["security_controls"] = (
            aws_sdk_securityhub.types.security_controls.deserialize_json(
                data["SecurityControls"]
            )
        )
    if "UnprocessedIds" in data:
        import aws_sdk_securityhub.types.unprocessed_security_controls

        out["unprocessed_ids"] = (
            aws_sdk_securityhub.types.unprocessed_security_controls.deserialize_json(
                data["UnprocessedIds"]
            )
        )
    return out
