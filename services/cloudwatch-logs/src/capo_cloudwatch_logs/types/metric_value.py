"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#MetricValue``."""

from typing import TypeAlias

"""<p>The value to publish to the CloudWatch metric. For example, if you're counting the occurrences of a term like <code>Error</code>, the value is <code>1</code> for each occurrence. If you're counting the bytes transferred, the value is the value in the log event.</p>"""
MetricValue: TypeAlias = str
