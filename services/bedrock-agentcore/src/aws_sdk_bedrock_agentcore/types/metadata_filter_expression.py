"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MetadataFilterExpression``."""

from typing import TypeAlias

"""<p> A JSON document that represents a structured metadata filter expression. Supports field-level operators (<code>$eq</code>, <code>$ne</code>, <code>$in</code>) and logical operators (<code>$and</code>, <code>$or</code>) on filterable fields (<code>name</code>, <code>descriptorType</code>, <code>version</code>).</p>"""
MetadataFilterExpression: TypeAlias = object
