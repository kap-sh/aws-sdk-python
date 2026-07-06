"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetRegisterAccountStatusRequest``."""

from typing_extensions import TypedDict


class GetRegisterAccountStatusRequest(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRegisterAccountStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRegisterAccountStatusRequest:
    out: GetRegisterAccountStatusRequest = {}  # type: ignore[typeddict-item]
    return out
