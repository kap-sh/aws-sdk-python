"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#Assertion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.assertion_source
    import aws_sdk_resiliencehubv2.types.assertion_text
    import aws_sdk_resiliencehubv2.types.uuid


class Assertion(TypedDict):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    assertion_id: "aws_sdk_resiliencehubv2.types.uuid.Uuid"
    """<p>The unique identifier of the assertion.</p>"""
    text: "aws_sdk_resiliencehubv2.types.assertion_text.AssertionText"
    """<p>The text content of the assertion.</p>"""
    source: "aws_sdk_resiliencehubv2.types.assertion_source.AssertionSource"
    """<p>The source of the assertion, indicating whether it was AI-generated or created by a user.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the assertion was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the assertion was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Assertion) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["assertionId"] = value["assertion_id"]
    out["text"] = value["text"]
    import aws_sdk_resiliencehubv2.types.assertion_source

    out["source"] = aws_sdk_resiliencehubv2.types.assertion_source.serialize_json(
        value["source"]
    )
    if "created_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> Assertion:
    out: Assertion = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("Assertion.service_arn required")
    if "assertionId" in data:
        out["assertion_id"] = data["assertionId"]
    else:
        raise DeserializationError("Assertion.assertion_id required")
    if "text" in data:
        out["text"] = data["text"]
    else:
        raise DeserializationError("Assertion.text required")
    if "source" in data:
        import aws_sdk_resiliencehubv2.types.assertion_source

        out["source"] = aws_sdk_resiliencehubv2.types.assertion_source.deserialize_json(
            data["source"]
        )
    else:
        raise DeserializationError("Assertion.source required")
    if "createdAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
