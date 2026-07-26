"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchGetSecurityControlsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.string_list


class BatchGetSecurityControlsRequest(TypedDict, closed=True):
    security_control_ids: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p> A list of security controls (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters). The security control ID or Amazon Resource Name (ARN) is the same across standards. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSecurityControlsRequest) -> dict:
    out: dict = {}
    if "security_control_ids" in value:
        import capo_securityhub.types.string_list

        out["SecurityControlIds"] = capo_securityhub.types.string_list.serialize_json(
            value["security_control_ids"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetSecurityControlsRequest:
    out: BatchGetSecurityControlsRequest = {}  # type: ignore[typeddict-item]
    if "SecurityControlIds" in data:
        import capo_securityhub.types.string_list

        out["security_control_ids"] = (
            capo_securityhub.types.string_list.deserialize_json(
                data["SecurityControlIds"]
            )
        )
    return out
