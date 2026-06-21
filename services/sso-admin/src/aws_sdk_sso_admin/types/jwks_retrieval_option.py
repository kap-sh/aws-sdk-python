"""Generated from Smithy shape ``com.amazonaws.ssoadmin#JwksRetrievalOption``."""

from typing import Literal, TypeAlias, cast

JwksRetrievalOption: TypeAlias = Literal["OPEN_ID_DISCOVERY",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JwksRetrievalOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JwksRetrievalOption:
    return cast(JwksRetrievalOption, data)
