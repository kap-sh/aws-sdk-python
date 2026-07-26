"""Generated from Smithy shape ``com.amazonaws.sesv2#ListRecommendationsFilterKey``."""

from typing import Literal, TypeAlias, cast

"""<p>The <code>ListRecommendations</code> filter type. This can be one of the following:</p> <ul> <li> <p> <code>TYPE</code> – The recommendation type, with values like <code>DKIM</code>, <code>SPF</code>, <code>DMARC</code>, <code>BIMI</code>, or <code>COMPLAINT</code>.</p> </li> <li> <p> <code>IMPACT</code> – The recommendation impact, with values like <code>HIGH</code> or <code>LOW</code>.</p> </li> <li> <p> <code>STATUS</code> – The recommendation status, with values like <code>OPEN</code> or <code>FIXED</code>.</p> </li> <li> <p> <code>RESOURCE_ARN</code> – The resource affected by the recommendation, with values like <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>.</p> </li> </ul>"""
ListRecommendationsFilterKey: TypeAlias = Literal[
    "TYPE",
    "IMPACT",
    "STATUS",
    "RESOURCE_ARN",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsFilterKey) -> str:
    return value


def deserialize_json(data: str) -> ListRecommendationsFilterKey:
    return cast(ListRecommendationsFilterKey, data)
