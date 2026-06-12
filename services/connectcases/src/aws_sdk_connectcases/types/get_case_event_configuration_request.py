"""Generated from Smithy shape ``com.amazonaws.connectcases#GetCaseEventConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_id


class GetCaseEventConfigurationRequest(TypedDict):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseEventConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCaseEventConfigurationRequest:
    out: GetCaseEventConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
