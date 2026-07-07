"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationAlreadyExists``."""

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import ServiceError


class AssociationAlreadyExists_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationAlreadyExists_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationAlreadyExists_:
    out: AssociationAlreadyExists_ = {}  # type: ignore[typeddict-item]
    return out


class AssociationAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#AssociationAlreadyExists``."""

    code: str | None = "AssociationAlreadyExists"

    def __init__(self, data: AssociationAlreadyExists_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AssociationAlreadyExists",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AssociationAlreadyExists":
        return cls(deserialize_aws_json_1_1(data))
