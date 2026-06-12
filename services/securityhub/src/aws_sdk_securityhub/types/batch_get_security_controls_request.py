"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchGetSecurityControlsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.string_list


class BatchGetSecurityControlsRequest(TypedDict):
    security_control_ids: NotRequired[
        "aws_sdk_securityhub.types.string_list.StringList"
    ]
    """<p> A list of security controls (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters). The security control ID or Amazon Resource Name (ARN) is the same across standards. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSecurityControlsRequest) -> dict:
    out: dict = {}
    if "security_control_ids" in value:
        import aws_sdk_securityhub.types.string_list

        out["SecurityControlIds"] = (
            aws_sdk_securityhub.types.string_list.serialize_json(
                value["security_control_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetSecurityControlsRequest:
    out: BatchGetSecurityControlsRequest = {}  # type: ignore[typeddict-item]
    if "SecurityControlIds" in data:
        import aws_sdk_securityhub.types.string_list

        out["security_control_ids"] = (
            aws_sdk_securityhub.types.string_list.deserialize_json(
                data["SecurityControlIds"]
            )
        )
    return out
